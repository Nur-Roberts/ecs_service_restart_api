import boto3

# initiate client
ecs_client = boto3.client('ecs')


def restart_ecs_service(cluster_name,service_name):
    try:

        response = ecs_client.update_service(
            cluster='ecs-lab-2-cluster',
            service='worker',
            forceNewDeployment=True
        )
        rollout_state = response['service']['deployments'][0]['rolloutState']
        rollout_state_reason = response['service']['deployments'][0]['rolloutStateReason']
    except Exception as error:
        rollout_state = "Error"
        rollout_state_reason = str(error)

    return rollout_state, rollout_state_reason