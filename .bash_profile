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
export FUN=$DESKTOP/fun
export BACKUP=$DESKTOP/backup
export TEST=$DESKTOP/test
export TODO=$DESKTOP/todo
export BOOK=$DESKTOP/book
export DOC=$HOME/Documents
function co {
    if (( $# == 0 )); then
        echo "usage: $FUNCNAME [11601|11642|15513|15605|15611|15618|15619|18641|18746|18756|18798|18842]"
        echo "11601 Coding Boot Camp"
        echo "11642 Search Engines"
        echo "15513 Introduction To Computer System"
        echo "15605 Operating System Design and Implementaion"
        echo "15611 Compiler Design"
        echo "15618 Parallel Computer Architecture and Programming"
        echo "15619 Cloud Computing"
        echo "18641 Java for Smartphone Development"
        echo "18746 Storage Systems"
        echo "18756 Packet Switching and Computer Networks"
        echo "18798 Image, Video, and Multimedia"
        echo "18842 Distributed Systems"
        return
    fi
    case $1 in
        11601) cd "$CMU/11601 Coding Boot Camp";;
        11642) cd "$CMU/11642 Search Engines";;
        15513) cd "$CMU/15513 Introduction To Computer System";;
        15605) cd "$CMU/15605 Operating System Design and Implementaion";;
        15611) cd "$CMU/15611 Compiler Design";;
        15618) cd "$CMU/15618 Parallel Computer Architecture and Programming";;
        15619) cd "$CMU/15619 Cloud Computing";;
        18641) cd "$CMU/18641 Java for Smartphone Development";;
        18746) cd "$CMU/18746 Storage Systems";;
        18756) cd "$CMU/18756 Packet Switching and Computer Networks";;
        18798) cd "$CMU/18798 Image, Video, and Multimedia";;
        18842) cd "$CMU/18842 Distributed Systems";;
        *) echo "unknown parameter" ;;
    esac
}

