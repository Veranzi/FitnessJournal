# Deploying Fitness Journal on Render

This guide will walk you through deploying your Django fitness journal application on Render.

## Prerequisites

- A Render account (free tier available)
- Your Django project pushed to a Git repository (GitHub, GitLab, etc.)

## Step 1: Prepare Your Repository

Make sure your repository contains all the necessary files we just created:

- `requirements.txt` - Python dependencies
- `build.sh` - Build script for Render
- `render.yaml` - Render configuration
- `fitness_journal/settings_production.py` - Production settings
- `.gitignore` - Excludes unnecessary files

## Step 2: Push to Git

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

## Step 3: Deploy on Render

### Option A: Using render.yaml (Recommended)

1. Go to [render.com](https://render.com) and sign in
2. Click "New +" and select "Blueprint"
3. Connect your Git repository
4. Render will automatically detect the `render.yaml` file
5. Click "Apply" to create your services

### Option B: Manual Setup

1. Go to [render.com](https://render.com) and sign in
2. Click "New +" and select "Web Service"
3. Connect your Git repository
4. Configure the service:
   - **Name**: `fitness-journal`
   - **Environment**: `Python 3`
   - **Build Command**: `chmod +x build.sh && ./build.sh`
   - **Start Command**: `gunicorn fitness_journal.wsgi:application`
   - **Plan**: Free

5. Add environment variables:
   - `DJANGO_SETTINGS_MODULE`: `fitness_journal.settings_production`
   - `SECRET_KEY`: Generate a new secret key
   - `PYTHON_VERSION`: `3.11.0`

6. Create a PostgreSQL database:
   - Click "New +" → "PostgreSQL"
   - Name: `fitness-journal-db`
   - Plan: Free
   - Copy the connection string

7. Add the database URL to your web service environment variables:
   - `DATABASE_URL`: Paste the connection string from step 6

## Step 4: Configure Custom Domain (Optional)

1. In your web service settings, go to "Settings" → "Custom Domains"
2. Add your domain and configure DNS records
3. Enable HTTPS (Render provides free SSL certificates)

## Step 5: Monitor and Maintain

- Check the "Logs" tab for any errors
- Monitor your database usage
- Set up alerts for downtime

## Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `DJANGO_SETTINGS_MODULE` | Django settings module | Yes |
| `SECRET_KEY` | Django secret key | Yes |
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `PYTHON_VERSION` | Python version | Yes |

## Troubleshooting

### Common Issues

1. **Build fails**: Check the build logs for missing dependencies
2. **Database connection error**: Verify `DATABASE_URL` is set correctly
3. **Static files not loading**: Ensure `build.sh` runs successfully
4. **500 errors**: Check Django logs in Render dashboard

### Debug Mode

To temporarily enable debug mode for troubleshooting:
1. Add `DEBUG=True` to environment variables
2. Redeploy the service
3. Check logs for detailed error messages

## Security Notes

- Never commit sensitive information like API keys
- Use environment variables for all secrets
- Keep your dependencies updated
- Consider enabling HTTPS for production use

## Cost Optimization

- Free tier includes:
  - 750 hours/month of web service runtime
  - 1GB PostgreSQL database
  - 100GB bandwidth/month
- Monitor usage to avoid unexpected charges
- Consider upgrading to paid plans for production use

## Support

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Render Community](https://community.render.com/)