import boto3
import os

# initiate aws client for ECS service
ecs_client = boto3.client('ecs', region_name=os.environ["aws_region"])

def restart_ecs_service(cluster_name,service_name):
    try:
        response = ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            forceNewDeployment=True #Trigger forced deployment which in essence replace the previous and result in a "restarted service"
        )
        rollout_state = response['service']['deployments'][0]['rolloutState']
        rollout_state_reason = response['service']['deployments'][0]['rolloutStateReason']
    except Exception as error:
        rollout_state = "Error"
        rollout_state_reason = str(error)

    return rollout_state, rollout_state_reason