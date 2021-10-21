---
title: "3. Configure AWS Command Line Interface (CLI) for CDK"
chapter: true
weight: 18
---

## Configure AWS CLI

1. Using the credentials from step 1 login to your AWS account.

2. Select **IAM** in the list of services, and click **Users**
   ![IAM User](/images/setup/setup_iam_user.png)

3. Open the user you created earlier. Click **Create Access Key** and save both Access Key ID and Secret Access Key

{{% notice warning %}}
   Both Access Key ID and Secret Access Key are sensitive information. <span style="color: red;">**Do not be store or publish it publicly**</span>.
   {{% /notice %}}
   
   ![Create Access Key](/images/setup/setup_create_access_key.png)


4. Install AWS CLI using the instructions from the link below
   https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html 

5. Install AWS CDK on your machine using the link below
   https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install



   {{% notice warning %}}
   If the IAM role is not valid, <span style="color: red;">**DO NOT PROCEED**</span>. Go back and confirm the steps on this page.
   {{% /notice %}}

   If you are done, please proceed to the Partner Setup section!