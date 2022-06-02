# this builds app to complete executable with pyinstaller

python_file_name="./main"


echo "building app"
pyinstaller "$python_file_name.py"
# add dependencies
cp "./default_config.json" "./dist/$python_file_name/default_config.json"
cp -r "./resources" "./dist/$python_file_name/resources"
