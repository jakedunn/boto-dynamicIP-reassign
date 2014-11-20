Simple script to adjust IP adresses which are allowed acesses via ssh to current system IP Adress.
Obvious security flaw is compromise of IAM User credentials. or http://wtfismyip.com is down

Made for Matt by Jake.
Absolutly No Warranty or gaurentee provided =]

You will need to make an IAM user with this access profile:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "ec2:*",
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

Yes technically it is allowed all actions, I will leave it as a learning excersise for you to lock it down to only have contorl on security groups. ie. I cbf.

Drop in the credetials, your region, and the name of the security group in the relevant variables.

MIT Liscense. Do whatever you want with it. If you sell and make $$$ I would appreciate beer.