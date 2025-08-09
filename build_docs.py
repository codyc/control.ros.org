#!/usr/bin/env python3
"""
Sphinx文档构建脚本
"""
import os
import subprocess
import sys
import shutil

def check_environment():
    """检查环境是否正确设置"""
    # 检查是否在虚拟环境中
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  警告：你可能没有在虚拟环境中运行")
        print("建议先激活虚拟环境：.\\venv\\Scripts\\Activate.ps1")
        
    # 检查必要的包
    try:
        import sphinx
        print(f"✅ Sphinx版本：{sphinx.__version__}")
    except ImportError:
        print("❌ Sphinx未安装")
        return False
        
    try:
        import sphinx_multiversion
        print(f"✅ sphinx-multiversion版本：{sphinx_multiversion.__version__}")
    except ImportError:
        print("❌ sphinx-multiversion未安装")
        return False
        
    return True

def build_single_version():
    """构建单个版本的文档"""
    print("构建单个版本的文档...")
    # 跳过有问题的generate_parameter_library扩展
    extensions_override = "sphinx.ext.intersphinx,sphinx.ext.todo,sphinx.ext.githubpages,sphinx_rtd_theme,sphinx_multiversion,sphinx_copybutton,sphinx_tabs.tabs,sphinx.ext.autosectionlabel,myst_parser"
    
    cmd = [
        "sphinx-build",
        "-b", "html",
        ".",
        "_build/html",
        "-D", f"extensions={extensions_override}"
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ 单版本构建成功！输出目录：_build/html")
        print("🌐 打开文档：Start-Process _build/html/index.html")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 构建失败：{e}")
        if e.stdout:
            print("标准输出：", e.stdout[-1000:])  # 只显示最后1000个字符
        if e.stderr:
            print("错误输出：", e.stderr[-1000:])  # 只显示最后1000个字符
        return False
    except FileNotFoundError:
        print("❌ 找不到sphinx-build命令，请确保Sphinx已正确安装")
        return False

def build_multiversion():
    """构建多版本文档"""
    print("构建多版本文档...")
    
    # 检查是否在git仓库中
    if not os.path.exists(".git"):
        print("❌ 当前目录不是git仓库，sphinx-multiversion需要在git仓库中运行")
        return False
    
    cmd = [
        "sphinx-multiversion",
        ".",
        "_build/multiversion"
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ 多版本构建成功！输出目录：_build/multiversion")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 多版本构建失败：{e}")
        if e.stdout:
            print("标准输出：", e.stdout)
        if e.stderr:
            print("错误输出：", e.stderr)
        print("提示：确保你在一个git仓库中，并且配置了正确的分支设置")
        return False
    except FileNotFoundError:
        print("❌ 找不到sphinx-multiversion命令，请确保已正确安装")
        return False

def clean_build():
    """清理构建目录"""
    print("清理构建目录...")
    if os.path.exists("_build"):
        shutil.rmtree("_build")
        print("✅ 构建目录已清理")
    else:
        print("构建目录不存在，无需清理")

def main():
    """主函数"""
    print("=== Sphinx文档构建工具 ===")
    
    # 检查环境
    if not check_environment():
        print("❌ 环境检查失败，请修复后重试")
        return
    
    # 如果有命令行参数，直接执行
    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "single":
            build_single_version()
        elif action == "multi":
            build_multiversion()
        elif action == "clean":
            clean_build()
        else:
            print("无效参数。用法：python build_docs.py [single|multi|clean]")
        return
    
    # 交互式菜单
    print("1. 构建单个版本")
    print("2. 构建多版本")
    print("3. 清理构建目录")
    print("4. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-4): ").strip()
        
        if choice == "1":
            build_single_version()
        elif choice == "2":
            build_multiversion()
        elif choice == "3":
            clean_build()
        elif choice == "4":
            print("退出构建工具")
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()
