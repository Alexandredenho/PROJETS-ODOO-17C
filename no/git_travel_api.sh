rm -r addons/travel_api
rm -rf .git/modules/travel_api
git rm --cached addons/travel_api
git submodule update --force --init --recursive