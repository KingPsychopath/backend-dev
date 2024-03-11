###############################################################################
# Compare-Dif.ps1
# Copyright (c) 2024 - KingPsychopath
#
# Do whatever you want with this module. It's free to use and modify.
###############################################################################

Param(
  [Parameter(Position=0)]
  [string]$a,
  [Parameter(Position=1)]
  [string]$b
)

$totalFilesA = (Get-ChildItem -Recurse -path $a).Count
$totalFilesB = (Get-ChildItem -Recurse -path $b).Count
$totalFiles = $totalFilesA + $totalFilesB

$fsa = Get-ChildItem -Recurse -path $a | ForEach-Object -Begin { $i=0 } -Process {
    $i++
    Write-Progress -Activity "Scanning directory A" -Status "$i out of $totalFilesA files processed" -PercentComplete ($i/$totalFilesA*100)
    $_
}

$fsb = Get-ChildItem -Recurse -path $b | ForEach-Object -Begin { $i=0 } -Process {
    $i++
    Write-Progress -Activity "Scanning directory B" -Status "$i out of $totalFilesB files processed" -PercentComplete ($i/$totalFilesB*100)
    $_
}

Compare-Object -ReferenceObject $fsa -DifferenceObject $fsb