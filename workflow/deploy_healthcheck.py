from workflow.flows.healthcheck import healthcheck

if __name__ == '__main__':
    healthcheck.serve(name='rx-healthcheck',
                    description='Healthcheck pipeline')