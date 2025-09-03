# freyberg-dvc-01
Repo for testing Freyberg DVC setup




https://github.com/iterative/dvc/issues/7372#issuecomment-1036654393

#!/bin/bash
git init b2-dvc-test
pushd b2-dvc-test
virtualenv venv
source venv/bin/activate
pip install dvc[s3] > /dev/null
dvc init
mkdir data
echo "test data1" > data/test1.txt
echo "test data2" > data/test2.txt
echo "test data3" > data/test3.txt
dvc add data
dvc remote add -d b2 s3://dvc-test/objs
dvc remote modify b2 endpointurl https://s3.us-west-000.backblazeb2.com
dvc remote modify --local b2 access_key_id ***
dvc remote modify --local b2 secret_access_key ***
dvc push -v
sleep 2
dvc doctor
popd 
rm -rf b2-dvc-test





(dvc_test) C:\Users\jbennett\repos\freyberg-dvc-01>dvc remote add -d b2 s3://freyberg-dvc
Setting 'b2' as a default remote.

(dvc_test) C:\Users\jbennett\repos\freyberg-dvc-01>dvc remote modify b2 endpointurl https://s3.us-west-004.backblazeb2.com

(dvc_test) C:\Users\jbennett\repos\freyberg-dvc-01>dvc remote modify --local b2 access_key_id 004e013c639b44b0000000003

(dvc_test) C:\Users\jbennett\repos\freyberg-dvc-01>dvc remote modify --local b2 secret_access_key <key>

(dvc_test) C:\Users\jbennett\repos\freyberg-dvc-01>dvc push -v