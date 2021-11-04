---
title: "Introduction"
chapter: true
weight: 1
---

# AWS x Snyk Code Tools Integration

### Welcome

In this workshop, you will learn how to integrate Snyk with the AWS Code Tools (Code Commit, Code Build & Code Artifact)

> This workshop is focused on scanning Python packages. You can apply similar design and automation for other languages supported by Snyk.

### Learning Objectives
- Deploy an AWS CodePipeline which scans a list of Code Commit repositories automatically upon commit using Snky
- Deploy a Code Pipeline to scan an entire Code Artifact Domain containing Python packages
- Deploy an AWS IAM role to enable Snyk to scan containers in ECR repositories

{{% notice warning %}}
<p style='text-align: left;'>
The examples and sample code provided in this workshop are intended to be consumed as instructional content. These will help you understand how various AWS services can be architected to build a solution while demonstrating best practices along the way. These examples are not intended for use in production environments.
</p>
{{% /notice %}}
