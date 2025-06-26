#!/usr/bin/env python3
"""
Build and publish script for hs-django-admin package
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def clean_build():
    """Clean previous build artifacts"""
    print("\n🧹 Cleaning previous build artifacts...")
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for pattern in dirs_to_clean:
        for path in Path('.').glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"   Removed {path}")
            elif path.is_file():
                path.unlink()
                print(f"   Removed {path}")

def check_manifest():
    """Check if MANIFEST.in is properly configured"""
    print("\n📋 Checking MANIFEST.in...")
    if not run_command("check-manifest", "Manifest check"):
        print("⚠️  Manifest check failed. You may need to update MANIFEST.in")
        return False
    return True

def build_package():
    """Build the package"""
    print("\n🔨 Building package...")
    if not run_command("python -m build", "Package build"):
        return False
    return True

def check_package():
    """Check the built package"""
    print("\n🔍 Checking built package...")
    if not run_command("twine check dist/*", "Package check"):
        return False
    return True

def upload_to_testpypi():
    """Upload to TestPyPI"""
    print("\n📤 Uploading to TestPyPI...")
    if not run_command("twine upload --repository testpypi dist/*", "TestPyPI upload"):
        return False
    return True

def upload_to_pypi():
    """Upload to PyPI"""
    print("\n📤 Uploading to PyPI...")
    if not run_command("twine upload dist/*", "PyPI upload"):
        return False
    return True

def main():
    """Main build process"""
    print("🚀 HS Django Admin Package Builder")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path('setup.py').exists():
        print("❌ setup.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Check manifest
    if not check_manifest():
        print("⚠️  Continuing despite manifest check failure...")
    
    # Build package
    if not build_package():
        print("❌ Build failed. Exiting.")
        sys.exit(1)
    
    # Check package
    if not check_package():
        print("❌ Package check failed. Exiting.")
        sys.exit(1)
    
    print("\n✅ Package built successfully!")
    print("\n📦 Next steps:")
    print("1. Test the package: pip install --index-url https://test.pypi.org/himel.py/hs-django-admin")
    print("2. Upload to TestPyPI: python build_package.py --test")
    print("3. Upload to PyPI: python build_package.py --publish")
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--test':
            if upload_to_testpypi():
                print("\n✅ Successfully uploaded to TestPyPI!")
            else:
                print("\n❌ Failed to upload to TestPyPI")
                sys.exit(1)
        elif sys.argv[1] == '--publish':
            if upload_to_pypi():
                print("\n✅ Successfully uploaded to PyPI!")
            else:
                print("\n❌ Failed to upload to PyPI")
                sys.exit(1)

if __name__ == "__main__":
    main() 