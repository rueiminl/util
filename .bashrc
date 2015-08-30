function co {
    if (( $# == 0 )); then
        echo "usage: $FUNCNAME [15513|15605|15618|15619|18756|18842]"
        return
    fi
    case $1 in
        15513) cd "$CMU/15513 Introduction To Computer System";;
        15605) cd "$CMU/15605 Operating System Design and Implementaion";;
        15618) cd "$CMU/15618 Parallel Computer Architecture and Programming";;
        15619) cd "$CMU/15619 Cloud Computing";;
        18756) cd "$CMU/18756 Packet Switching and Computer Networks";;
        18842) cd "$CMU/18842 Distributed Systems";;
        *) echo "unknown parameter" ;;
    esac
}
