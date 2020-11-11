Object detection
========
The anaconda enviroments include all the libraries


**Run neural network**

set run-tf1_15.yml enviroment in anaconda

~~~~~~~~~~~~~~~~~
  conda env create -f run-tf1_15.yml
  conda activate run-tf1_15
  cd/models/research/object_detection
  python webcam_detection.py
~~~~~~~~~~~~~~~~~


**Train neural network**


set train-tf1_15.yml enviroment in anaconda

~~~~~~~~~~~~~~~~~
  conda env create -f train-tf1_15.yml
  conda activate train-tf1_15

  cd labelimg

  #custom images
  pyrcc5 -o libs/resources.py resources.qrc
  python labelImg.py

  cd..
  cd models/research/object_detection/images
  python xml_to_csv.py

  #data record
  cd..
  python generate_tfrecord.py --csv_input=data/test_labels.csv --output_path=data/test.record --image_dir=images/test

  python generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record --image_dir=images/train

  #set path
  cd ../..
  cd ..
  set PYTHONPATH=$PYTHONATH:`pwd`:`pwd/slim

  cd models/research/object_detection/

  #train neural netkowrk
  python train.py --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_pets.config --logtostderr

  #export neural network
  python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training/model.ckpt-3207 --output_directory new_graph

  python custom_model_webcam.py
  ~~~~~~~~~~~~~~~~~
