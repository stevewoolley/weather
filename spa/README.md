# Single Page Application (SPA)Deployment

### Install packages and dependencies
```bash
cd $PROJECT_DIRECTORY/spa
npm install
```
Should generate package-lock.json file suitable for framing.

### 

### Start the package
```bash
cd $PROJECT_DIRECTORY/spa
npm start
```
Should run the start up scripts (referencing the local package.json).

### Build a deployment file
```bash
npm run build
```
Will generate the required artifacts for deployment to a host.

### Example: Deploy to AWS S3 bucket for static hosting
*Assuming aws cli tools are installed.*
```bash
cd $PROJECT_DIRECTORY/spa/build
aws s3 sync . s3://YOUR_BUCKET_FOR_HOSTING --acl public-read
```
