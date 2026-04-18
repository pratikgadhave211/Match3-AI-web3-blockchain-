# Match3 AI Web3 Blockchain

Split deployment setup:
- Frontend: Vercel
- Backend: Render

## Backend (Render)

This repository includes a Render blueprint at `render.yaml`.

### Option A: Blueprint deploy
1. In Render, click `New +` -> `Blueprint`.
2. Select this GitHub repository.
3. Confirm `render.yaml` is detected and deploy.
4. Fill any `sync: false` environment variables in Render.

### Option B: Manual Web Service deploy
1. Create a new `Web Service` in Render from this repository.
2. Use these settings:
	- Runtime: `Python`
	- Build Command: `pip install -r requirements.txt`
	- Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
3. Add environment variables:
	- `HUGGINGFACEHUB_API_TOKEN`
	- `RPC_URL`
	- `CONTRACT_ADDRESS`
	- `EXPECTED_CHAIN_ID` (example: `11155111`)
	- `NETWORK_NAME` (example: `Sepolia Test Network`)
	- `FRONTEND_ORIGIN` (your Vercel frontend URL; comma-separate if multiple)

## Frontend (Vercel)

Deploy the `frontend` folder as a Vercel project.

### Vercel project settings
- Framework Preset: `Vite`
- Root Directory: `frontend`
- Build Command: `npm run build`
- Output Directory: `dist`

### Required frontend env variable
Set in Vercel project env vars:
- `VITE_API_BASE_URL=https://<your-render-service>.onrender.com`

Then redeploy frontend after saving env variables.

## CORS Notes

Backend CORS allows:
- Localhost dev ports
- Any `*.vercel.app` origin
- Additional explicit origins from `FRONTEND_ORIGIN`

If you use a custom domain on Vercel, add it to `FRONTEND_ORIGIN` in Render.
