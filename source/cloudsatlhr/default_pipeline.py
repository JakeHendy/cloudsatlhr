from aws_cdk import core, pipelines, aws_codebuild as codebuild, aws_codepipeline as codepipeline, aws_codepipeline_actions as actions

from cloudsatlhr.acquisition_stack import AcquisitionStack

class DefaultPipeline(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly = codepipeline.Artifact()
        
        build_environment = codebuild.BuildEnvironment(
            build_image=codebuild.LinuxBuildImage.AMAZON_LINUX_2_3
        )

        the_pipeline = pipelines.CdkPipeline(self, "Pipeline",
            pipeline_name="DefaultPipeline",
            cloud_assembly_artifact=cloud_assembly,
            source_action=actions.GitHubSourceAction(
                action_name="GitHub",
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager("github-token"),
                owner="JakeHendy",
                repo="cloudsatlhr"
            ),

            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                subdirectory="source",
                synth_command="npx cdk synth",
                install_command="pip install -r requirements.txt",
                environment=build_environment,
                cloud_assembly_artifact=cloud_assembly
                )
        )
        the_pipeline.add_application_stage(AcquisitionStack(self, "AcqusitionStackDev"))

        # The code that defines your stack goes here 
