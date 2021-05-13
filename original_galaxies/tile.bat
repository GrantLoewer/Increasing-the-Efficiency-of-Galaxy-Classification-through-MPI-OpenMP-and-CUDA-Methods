for %%f in (*.tif) do (if not exist "./%%~nf" mkdir %%~nf
for /l %%x in (0, 1, 111) do (for /l %%y in (0, 1, 111) do (
magick convert -define tif:size=120x120 %%f[9x9+%%x+%%y] "./%%~nf/%%~nf %%xx%%y.tif"
)))
pause