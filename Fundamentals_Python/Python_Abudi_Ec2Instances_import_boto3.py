import boto3

def launch_instances(image_id, region):
    # Define the EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    # Launch the first EC2 instance
    response1 = ec2_client.run_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    instance_id1 = response1['Instances'][0]['InstanceId']
    region1 = region
    print(f"Instance ID: {instance_id1}, Region: {region1}")

    # Launch the second EC2 instance in a different region
    if region == 'us-east-1':
        region2 = 'us-west-2'
    else:
        region2 = 'us-east-1'
    ec2_client2 = boto3.client('ec2', region_name=region2)
    response2 = ec2_client2.run_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    instance_id2 = response2['Instances'][0]['InstanceId']
    print(f"Instance ID: {instance_id2}, Region: {region2}")

    #The function launch_instances() takes two arguments, image_id and region.
     #It initializes an EC2 client in the specified region using the boto3 library.
#It launches the first EC2 instance using the run_instances() method of the EC2 client, passing in the image_id, MinCount, MaxCount, and InstanceType parameters.
#It extracts the instance_id1 and region1 from the response and prints them to the console.
#It then launches a second EC2 instance in a different region, using a simple if-else statement to determine the other region.
#It extracts the instance_id2 and prints it along with region2 to the console.
#To call this function, simply pass in the desired image_id and region as arguments:

launch_instances('ami-0123456789abcdef0', 'us-east-1')

#This will launch two EC2 instances in us-east-1 and us-west-2 regions with the specified image id.