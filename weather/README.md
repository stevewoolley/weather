# Lambda deployment

### Key Environment Variables
- *$PROJECT_DIRECTORY* - Self explanatory
- *$S3_BUCKET* - S3 bucket for deploying app
- *$OPENWEATHER_API_KEY* - API key provided for/by https://openweathermap.org
- *$CF_STACK_NAME* - Cloud Formation stack name    

### Build the lambda
```bash
sam build --template $PROJECT_DIRECTORY/template.yaml --build-dir $PROJECT_DIRECTORY/.aws-sam/build
```

### Package the lambda
```bash
sam package --template-file $PROJECT_DIRECTORY/.aws-sam/build/template.yaml --output-template-file $PROJECT_DIRECTORY/.aws-sam/build/packaged-template.yaml --s3-bucket $S3_BUCKET
```

### Deploy the lambda
```bash
sam deploy --template-file $PROJECT_DIRECTORY/.aws-sam/build/packaged-template.yaml --stack-name $CF_STACK_NAME --s3-bucket $S3_BUCKET --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --no-execute-changeset --parameter-overrides \"WeatherProviderApiKey\"=\"$OPENWEATHER_API_KEY\"
```