pip3 install -U Celery
pip3 install -U "celery[redis]"

########################################################################
###### MAC
export PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
export PROJECT_HOME=$HOME/
source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenvwrapper.sh
export JAVA_HOME=$(/usr/libexec/java_home)

source ~/.bash_profile

########################################################################
###### Let’s install Redis for the good. MAC
brew install redis
#Launch Redis on computer starts.
$ ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
#Start Redis server via “launchctl”.
$ launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
#Stop Redis on autostart on computer start.
$ launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
#Location of Redis configuration file.
/usr/local/etc/redis.conf
#Uninstall Redis and its files.
$ brew uninstall redis
$ rm ~/Library/LaunchAgents/homebrew.mxcl.redis.plist