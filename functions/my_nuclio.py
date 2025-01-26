import mlrun


def handler(context, event):
    project = mlrun.get_or_create_project("nuclio-trigger-workflow-amite", "/opt/nuclio")
    # project = mlrun.get_current_project()
    workflow_instance = project.run(
                            name="my-workflow",
                            watch=False,
                            # local=False,
                            engine="kfp",
                    )
    
