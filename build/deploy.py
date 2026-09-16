"""
Build System Deploy Module
==========================
Deploys built output to a directory for GitHub Pages. The deploy-dir (e.g. site/)
is a git clone of the public repo; it contains only built HTML, PDFs, and book.
"""

import shutil
import subprocess

from .book import Book
from .utils import print_step, print_success, print_error


def _git(deploy_dir, *args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(deploy_dir), capture_output=True, text=True)


def deploy(book: Book, run_build: bool = True, push: bool = False) -> bool:
    """
    Build and check the book (if run_build), then replace the contents of deploy-dir with
    the HTML output, keeping .git. If push=True, commit and push from deploy-dir.
    Returns True on success.
    """
    from .cli import build_all
    from .check import check

    deploy_dir = book.path(book.config.get("deploy-dir", "site"))
    deploy_repo = book.config.get("deploy-repo", "")

    if run_build:
        if not build_all(book):
            print_error("Build failed; not deploying.")
            return False
        if not check(book):
            print_error("Check failed; not deploying.")
            return False

    html_dir = book.html_dir
    if not html_dir.exists():
        print_error(f"HTML output not found: {html_dir}")
        print_error("Run './build.py all' first.")
        return False

    if not deploy_dir.exists():
        if deploy_repo:
            print_step(f"Cloning {deploy_repo} into {deploy_dir}...")
            result = subprocess.run(["git", "clone", deploy_repo, str(deploy_dir)], capture_output=True, text=True)
            if result.returncode != 0:
                print_error(f"git clone failed: {result.stderr}")
                return False
        else:
            deploy_dir.mkdir(parents=True)

    print_step(f"Deploying to {deploy_dir}...")
    git_dir = deploy_dir / ".git"
    for item in deploy_dir.iterdir():
        if item.name == ".git":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    for item in html_dir.iterdir():
        if item.is_dir():
            shutil.copytree(item, deploy_dir / item.name)
        else:
            shutil.copy2(item, deploy_dir / item.name)

    deploy_domain = book.config.get("deploy-domain", "")
    if deploy_domain:
        (deploy_dir / "CNAME").write_text(deploy_domain.strip(), encoding="utf-8")
    print_success(f"Deployed to {deploy_dir}")

    if not git_dir.exists():
        return True
    if not push:
        print_step(f"Next: cd {deploy_dir.name} && git add -A && git commit -m 'Deploy' && git push")
        return True

    print_step("Pushing to remote...")
    result = _git(deploy_dir, "add", "-A")
    if result.returncode != 0:
        print_error(f"git add failed: {result.stderr}")
        return False
    result = _git(deploy_dir, "commit", "-m", "Deploy")
    if result.returncode != 0:
        if "nothing to commit" not in result.stdout + result.stderr:
            print_error(f"git commit failed: {result.stderr}")
            return False
        print_success("No changes to commit.")
    push_url = book.config.get("deploy-push-url")
    result = _git(deploy_dir, "push", *([push_url, "HEAD"] if push_url else []))
    if result.returncode != 0:
        print_error(f"git push failed: {result.stderr}")
        return False
    print_success("Pushed to remote.")
    return True
