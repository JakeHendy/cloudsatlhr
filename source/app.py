#!/usr/bin/env python3

from aws_cdk import core

from cloudsatlhr.default_pipeline import DefaultPipeline

app = core.App()
DefaultPipeline(app, "DefaultPipeline")

app.synth()
