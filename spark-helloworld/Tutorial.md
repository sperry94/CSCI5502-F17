# Download Spark-EC2 program

https://github.com/amplab/spark-ec2

Download spark-ec2 from the link above.


# Set up an account in AWS
https://aws.amazon.com/

* Create a free account at the above link.
* Go to the AWS Management Console https://console.aws.amazon.com
* In the navigation bar, click on the location dropdown next to your name. Mine was "Oregon". Select "US West (Oregon)". !!!For this tutorial, make sure this is always set to "US West (Oregon)" anytime you do something in AWS!!!
* Click Services in the navigation bar and then click on ec2
* On the left bar under "Network & Security" select "Key Pairs"
* Click Create Key Pair and remember the name you give it (the name doesn't matter, I named mine "sparktest")
* A .pem file should download
* Click on your name in the navigation bar, then select "My Security Credentials"
* Under "Access keys", create a new access key
* Download the key file. Later when you need the AWS_SECRET_ACCESS_KEY and the AWS_ACCESS_KEY_ID, you will need to look in this file


# Start a Spark cluster on AWS

* Unzip the spark download
* Open a command line/terminal
* Navigate to the unzipped spark-ec2 directory
* To set up your terminal to be able to authenticate with AWS, run the following command (replace what's necessary): `export AWS_SECRET_ACCESS_KEY=<AWS secret access key>; export AWS_ACCESS_KEY_ID=<AWS access key>`
* To launch the spark cluster, run this command (replace what's necessary): `./spark-ec2 -k <key name> -i <key file location> -s 3 --instance-type=t2.micro --region=us-west-2 --zone=us-west-2b --ebs-vol-size=8 --spark-version=1.6.0 launch <enter a name for the cluster>`
* This will create a cluster of 4 spark 1.6.0 instances (1 master, 3 slaves) of type t2.micro (free) in the us-west region in the us-west-2b zone. Each instance will have 8GB of storage. NOTE: This step will take a while. You can go back to Services > EC2 (top nav bar) and then select Instances > Instances (left nav bar) to watch your instances start up. Also, if you see errors about not being able to ssh in (connection refused, etc), don't worry about it. This is just what is happening as the machine starts up. Eventually it will be able to connect. DO NOT STOP THE PROCESS, YOU WILL HAVE TO DELETE YOUR INSTANCES AND START OVER
* At this point, your cluster will be up and running.
* Check that it was successful by going to the UI page
  - Find the master hostname in the AWS console. Services -> EC2 (top nav bar), then Instances -> Instances (left nav bar). The name for this machine will have 'master' in it. You want the Public-DNS value
  - Go to <master hostname>:8080 in your browser, a UI page should appear.
*

You can also follow these instructions (in the Readme):
https://github.com/amplab/spark-ec2

# Submit a job to the Spark cluster
* Inside the wordcount folder of this repo folder, there will be two files, loremipsum.txt and wordcount.py
  - loremipsum.txt is a text file we will count the words for
  - wordcount.py is the spark program that will count the words
* Copy the wordcount folder onto the master machine.
  - Find its IP in the AWS console. Services -> EC2 (top nav bar), then Instances -> Instances (left nav bar). The name for this machine will have 'master' in it
  - Run the following command, replacing what's necessary: `scp -r -i <key file location> <path to wordcount folder> root@<master machine ip>:/user`
  - SSH into the master machine (run `ssh -i <key file location> root@<master machine ip>`) and make sure the files got copied
* Distribute these files to the HDFS for the cluster.
  - SSH into the master machine.
  - go into the ephemeral-hdfs/bin directory and run the following command: `./hadoop fs -copyFromLocal /user/wordcount/loremipsum.txt /user/wordcount/loremipsum.txt`
  - check the file is in the HDFS by running `./hadoop fs -ls /user/wordcount`
* Submit the job.
  - go back to the home directory. Then navigate to spark/bin
  - run this command `./spark-submit /user/wordcount.py`

Basic programming guide:
https://spark.apache.org/docs/1.6.0/quick-start.html
Examples:
https://spark.apache.org/examples.html

# Tear down your Spark cluster
* Go to the AWS Management Console https://console.aws.amazon.com
* Click Services in the navigation bar and then click on ec2
* Select Instances > Instances (left nav bar)
* Select all the spark instances (there should be 4)
* Right click on them and select 'Instance State' > Terminate
* You cluster should go offline

# References
* Lorem ipsum text for www.lipsum.com