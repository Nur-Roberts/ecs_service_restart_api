from flask import Flask, jsonify, request
from services.ecs_service import restart_ecs_service
import os

app = Flask(__name__)

@app.route('/api/v1/service_restart/<service_name>',methods=['POST'])
def service_restart(service_name):
    print(request.headers)
    cluster_name = request.headers.get('cluster_name')
    auth_id = request.headers.get('Authorization')
    service_name = service_name
    print(cluster_name)

    if auth_id == os.environ['auth_id']:
        rollout_state, rollout_state_reason = restart_ecs_service(cluster_name,service_name)
        return jsonify(
            rollout_state = rollout_state,
            rollout_state_reason = rollout_state_reason
        )
    else:
        return jsonify(
            unauthorized = "invalid or no auth token supplied"
        )

if __name__ == "__main__":
    app.run(debug=True)