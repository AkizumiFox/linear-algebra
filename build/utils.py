"""
Build System Utilities
======================
Helper functions for logging and formatting.
"""

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(msg):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{msg}{Colors.ENDC}")

def print_step(msg):
    print(f"{Colors.BLUE}==>{Colors.ENDC} {Colors.BOLD}{msg}{Colors.ENDC}")

def print_success(msg):
    print(f"{Colors.GREEN}✓{Colors.ENDC} {msg}")

def print_info(msg):
    print(f"{Colors.CYAN}ℹ{Colors.ENDC} {msg}")

def print_warning(msg):
    print(f"{Colors.WARNING}⚠ {msg}{Colors.ENDC}")

def print_error(msg):
    print(f"{Colors.FAIL}✖ {msg}{Colors.ENDC}")

def print_file_action(action, src, dst=None):
    if dst:
        print(f"  {Colors.CYAN}{action}{Colors.ENDC} {src} {Colors.BOLD}→{Colors.ENDC} {dst}")
    else:
        print(f"  {Colors.CYAN}{action}{Colors.ENDC} {src}")
