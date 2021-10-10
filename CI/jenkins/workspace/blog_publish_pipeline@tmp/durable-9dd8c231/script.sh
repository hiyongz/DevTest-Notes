
            cd ${env.repo_path}
            set -e # 告诉bash如果任何语句的执行结果为false则退出
            
            UPSTREAM=${1:-'@{u}'}
            LOCAL=$(git rev-parse @)
            REMOTE=$(git rev-parse "$UPSTREAM")
            BASE=$(git merge-base @ "$UPSTREAM")
            
            if [ $LOCAL = $REMOTE ]; then
                echo "Up-to-date"
            elif [ $LOCAL = $BASE ]; then
                echo "Need to pull"
                git pull    
            elif [ $REMOTE = $BASE ]; then
                echo "Need to push"
                git push
                
            fi
            
            if [ -n "$(git status -s | grep _posts)" ];then
                echo "blog changes"
                git add -A
                git commit -m "jenkins update"
                git push
                exit 0
            else
                echo "no blog changes"
                exit 1  #退出，jenkins会显示失败
            fi
            