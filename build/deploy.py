"""
Build System Deploy Module
==========================
Deploys built output to a directory for GitHub Pages. The deploy-dir (e.g. site/)
is a git clone of the public repo; it contains only built HTML, PDFs, and book.
"""

import subprocess
import shutil
from pathlib import Path

from .config import PROJECT_ROOT
from .utils import print_step, print_success, print_error


def deploy(config: dict, run_build: bool = True, push: bool = False) -> bool:
    """
    Build the site (if run_build) and copy _build/html to deploy-dir (e.g. site/).
    The deploy-dir should be a git clone of the public repo. Clears contents but
    preserves .git so you can commit and push only the built output.
    If push=True, runs git add, commit, push from deploy-dir.
    Returns True on success.
    """
    html_dir = PROJECT_ROOT / config["output"]["html"]
    deploy_dir = PROJECT_ROOT / config.get("deploy-dir", "site")
    deploy_repo = config.get("deploy-repo", "")

    if run_build:
        from .config import reset_counter_state
        from .html import build_html
        from .pdf import build_pdf, build_book
        from .manifest import scan_labels, generate_theorem_manifest, generate_navigation_manifest
        from .cli import extract_title_from_markdown, get_chapter_display_name

        reset_counter_state()
        scan_labels(config)

        def nav_manifest_wrapper(cfg, output_dir):
            generate_navigation_manifest(cfg, output_dir, extract_title_from_markdown)

        build_html(config, None, extract_title_from_markdown, get_chapter_display_name,
                   scan_labels, generate_theorem_manifest, nav_manifest_wrapper)
        build_pdf(config, None, extract_title_from_markdown, get_chapter_display_name)
        build_book(config)

    if not html_dir.exists():
        print_error(f"HTML output not found: {html_dir}")
        print_error("Run 'python build.py all' first.")
        return False

    # Clone if deploy-dir doesn't exist and deploy-repo is set
    if not deploy_dir.exists():
        if deploy_repo:
            print_step(f"Cloning {deploy_repo} into {deploy_dir}...")
            deploy_dir.parent.mkdir(parents=True, exist_ok=True)
            result = subprocess.run(
                ["git", "clone", deploy_repo, str(deploy_dir)],
                cwd=str(PROJECT_ROOT),
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print_error(f"git clone failed: {result.stderr}")
                return False
        else:
            deploy_dir.mkdir(parents=True, exist_ok=True)

    print_step(f"Deploying to {deploy_dir}...")

    # Clear deploy dir contents but preserve .git
    git_dir = deploy_dir / ".git"
    if git_dir.exists():
        for item in deploy_dir.iterdir():
            if item.name != ".git":
                if item.is_file():
                    item.unlink()
                else:
                    shutil.rmtree(item)
    else:
        if deploy_dir.exists():
            shutil.rmtree(deploy_dir)
        deploy_dir.mkdir(parents=True, exist_ok=True)

    # Copy built output
    for item in html_dir.iterdir():
        if item.is_file():
            shutil.copy2(item, deploy_dir / item.name)
        else:
            shutil.copytree(item, deploy_dir / item.name, dirs_exist_ok=True)

    # Add CNAME for GitHub Pages custom domain
    deploy_domain = config.get("deploy-domain", "")
    if deploy_domain:
        (deploy_dir / "CNAME").write_text(deploy_domain.strip(), encoding="utf-8")

    print_success(f"Deployed to {deploy_dir}")

    if push and git_dir.exists():
        print_step("Pushing to remote...")
        result = subprocess.run(
            ["git", "add", "-A"],
            cwd=str(deploy_dir),
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print_error(f"git add failed: {result.stderr}")
            return False
        result = subprocess.run(
            ["git", "commit", "-m", "Deploy"],
            cwd=str(deploy_dir),
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            if "nothing to commit" in (result.stdout or "") + (result.stderr or ""):
                print_success("No changes to commit.")
            else:
                print_error(f"git commit failed: {result.stderr}")
                return False
        result = subprocess.run(
            ["git", "push"],
            cwd=str(deploy_dir),
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print_error(f"git push failed: {result.stderr}")
            return False
        print_success("Pushed to remote.")
    elif git_dir.exists():
        print_step("Next: cd site && git add -A && git commit -m 'Deploy' && git push")
    return True
