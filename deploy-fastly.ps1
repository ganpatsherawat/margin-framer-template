# Fastly Direct Deployment Script (without GitHub Actions)
Param(
  [string]$FastlyToken = $env:FASTLY_API_TOKEN,
  [string]$ServiceId = ""
)

Write-Host "=== Fastly Deployment for HOOX Advisory ===" -ForegroundColor Cyan

# 1. Build project
Write-Host "1. Building static production assets via Astro..." -ForegroundColor Yellow
npm run build
if ($LASTEXITCODE -ne 0) {
  Write-Error "Astro build failed."
  exit 1
}

# 2. Check Fastly CLI
$fastlyBin = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Fastly.CLI_Microsoft.Winget.Source_8wekyb3d8bbwe\fastly.exe"
if (-not (Test-Path $fastlyBin)) {
  $fastlyCmd = Get-Command fastly -ErrorAction SilentlyContinue
  if ($fastlyCmd) { $fastlyBin = $fastlyCmd.Source }
}

if (-not (Test-Path $fastlyBin)) {
  Write-Error "Fastly CLI not found."
  exit 1
}

Write-Host "2. Using Fastly CLI: $fastlyBin" -ForegroundColor Green
& $fastlyBin version

# 3. Check Token
if (-not $FastlyToken) {
  Write-Host "No FASTLY_API_TOKEN detected." -ForegroundColor Yellow
  $FastlyToken = Read-Host "Please enter your Fastly API Token"
}

if (-not $FastlyToken) {
  Write-Error "Fastly API Token is required to deploy to Fastly."
  exit 1
}

# 4. Deploy package
Write-Host "3. Deploying to Fastly Compute..." -ForegroundColor Cyan
if ($ServiceId) {
  & $fastlyBin compute publish --token $FastlyToken --service-id $ServiceId --non-interactive --auto-yes
} else {
  & $fastlyBin compute publish --token $FastlyToken --non-interactive --auto-yes
}

Write-Host "=== Deployment finished ===" -ForegroundColor Green
