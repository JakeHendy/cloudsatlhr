#!/usr/bin/env python3

from aws_cdk import core

from source.source_stack import SourceStack


app = core.App()
SourceStack(app, "source")

app.synth()
