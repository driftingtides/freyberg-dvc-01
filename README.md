# freyberg-dvc-01
Repo for testing Freyberg DVC setup


### Create virtual environment

`conda create --name dvcenv`

`conda activate dvcenv`

`conda install dvc`


### Initializing dvc project
https://dvc.org/doc/start#initializing-a-project

`dvc init`

`git commit -m "Initialise DVC"`


### Preliminaries for testing with Freyberg
run `nodvc/preliminaries.py` to get the example Freyberg files

make data/models directory and copy freyberg_multilayer_transient into it

`dvc add data/models/freyberg_multilayer_transient`
`git add .gitignore' data\models\freyberg_multilayer_transient.dvc`
`git commit -m "Add freyberg data"`

Add google drive remote
`dvc remote add --default fr_mlay_trans gdrive://17Axlb5cr18vQblafTb9cDvfqD5Oe6NpC`                                             
Setting 'fr_mlay_trans' as a default remote.