export SUBLIME="$HOME/Library/Application Support/Sublime Text 3/Packages"
export CLICOLOR=1
export LSCOLORS=gxBxhxDxfxhxhxhxhxcxcx
export DROPBOX=$HOME/Dropbox
export REPO=$DROPBOX/repository
export DIARY=$REPO/diary
export LEETCODE=$HOME/Dropbox/repository/leetcode
export DESKTOP=$HOME/Desktop
export TEMP=$DESKTOP/temp
export PROJECT=$DESKTOP/project
export PROJ=$PROJECT
export ENOS=$PROJECT/enos/esnet/src/main/python
export JOB=$REPO/Job
export SHORTCUT=$DESKTOP/shortcut
export SC=$SHORTCUT
export CV=$PROJECT/simple-resume-cv
export DL=$HOME/Downloads
export UTIL=$PROJ/util
export CHIME=$PROJ/chimehacks2
export TRAV=$PROJ/team27/travelpad
export CMU=$REPO/CMU
function co {
    if (( $# == 0 )); then
        echo "usage: $FUNCNAME [15513|15605|15618|15619|18641|18746|18756|18842]"
        return
    fi
    case $1 in
        15513) cd "$CMU/15513 Introduction To Computer System";;
        15605) cd "$CMU/15605 Operating System Design and Implementaion";;
        15618) cd "$CMU/15618 Parallel Computer Architecture and Programming";;
        15619) cd "$CMU/15619 Cloud Computing";;
        18641) cd "$CMU/18641 Java for Smartphone Development";;
        18746) cd "$CMU/18746 Storage Systems";;
        18756) cd "$CMU/18756 Packet Switching and Computer Networks";;
        18842) cd "$CMU/18842 Distributed Systems";;
        *) echo "unknown parameter" ;;
    esac
}

