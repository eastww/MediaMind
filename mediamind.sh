#!/bin/bash

# MediaMind - 媒体智能管家
# 一键扫描和组织你的媒体库

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 显示使用方法
show_help() {
    echo "MediaMind - 媒体智能管家"
    echo ""
    echo "用法: $0 <目录> [选项]"
    echo ""
    echo "参数:"
    echo "  <目录>     媒体文件目录（必需）"
    echo ""
    echo "选项:"
    echo "  -h, --help     显示此帮助信息"
    echo "  --scan-only    只扫描，不整理"
    echo "  -v, --verbose  详细输出"
    echo ""
    echo "示例:"
    echo "  $0 v:/media/drama          # 整理电视剧"
    echo "  $0 v:/media --scan-only   # 只扫描"
    echo "  $0 v:/media -v            # 详细输出"
    echo ""
    echo "MediaMind会自动检测变化并只整理需要的内容！"
}

# 检查Python
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}错误: 未找到Python3${NC}"
        echo -e "${YELLOW}请安装Python 3.6或更高版本${NC}"
        exit 1
    fi
}

# 检查目录
check_directory() {
    local dir="$1"

    if [ ! -d "$dir" ]; then
        echo -e "${RED}错误: 目录不存在: $dir${NC}"
        exit 1
    fi
}

# 执行MediaMind
run_mind() {
    local dir="$1"
    local scan_only="$2"
    local verbose="$3"

    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local python_script="$script_dir/mediamind.py"

    if [ ! -f "$python_script" ]; then
        echo -e "${RED}错误: 找不到mediamind.py脚本${NC}"
        exit 1
    fi

    local cmd="python3 \"$python_script\" \"$dir\""

    if [ "$scan_only" = true ]; then
        cmd="$cmd --scan-only"
    fi

    if [ "$verbose" = true ]; then
        echo -e "${BLUE}正在执行: $cmd${NC}"
    fi

    if [ "$verbose" = true ]; then
        python3 "$python_script" "$dir" --scan-only
    else
        python3 "$python_script" "$dir"
    fi
}

# 主函数
main() {
    local directory=""
    local scan_only=false
    local verbose=false

    # 解析参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            --scan-only)
                scan_only=true
                shift
                ;;
            -v|--verbose)
                verbose=true
                shift
                ;;
            *)
                if [ -z "$directory" ]; then
                    directory="$1"
                    shift
                else
                    echo -e "${RED}错误: 多余的参数: $1${NC}"
                    exit 1
                fi
                ;;
        esac
    done

    # 检查必需参数
    if [ -z "$directory" ]; then
        echo -e "${RED}错误: 请指定媒体目录${NC}"
        show_help
        exit 1
    fi

    # 执行
    echo -e "${BLUE}🎬 MediaMind - 媒体智能管家${NC}"
    echo -e "${BLUE}=================================${NC}"
    echo ""

    check_python
    check_directory "$directory"
    run_mind "$directory" "$scan_only" "$verbose"

    echo ""
    echo -e "${GREEN}✨ MediaMind 完成！${NC}"
}

# 运行主函数
main "$@"