# -second_sem_project

Requirements mongodb python3 sarg analyser Sarg analyse requires some changes in configuration file as follows. 
In  /etc/sarg/sarg.cnf file change access_log path to your newly created directory.
ex. /home/rohit/project Uncomment the graph font and if given font exists in your system then ok else change it to available fonts. 
ex. /usr/share/fonts/truetype/ttf-khmeros-core/KhmerOSsys.ttf Change the output directory to your new created directory. 
ex. /home/rohit/project

To run the project- Create the new dirctory. Download the access.log file in the created directory link as
follows: https://drive.google.com/file/d/16D735kCqefO1Qltek_1vJWg5rw4-X0Ud/view?usp=sharing
Run the following python programs first. addedu.py addjoy.py addmat.py addmed.py addshop.py
If all five collections are created then run the following queries in in mongodb db.edu.createIndex({site:"text"}) db.joy.createIndex({site:"text"}) db.shop.createIndex({site:"text"}) db.med.createIndex({site:"text"}) db.mat.createIndex({site:"text"}) After setting up the sarg run the zero.py python program.
