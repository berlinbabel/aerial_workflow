# Adobe Lightroom

Applies to Lightroom 14.5.1

## Performance Issues

If lightroom is hanging when you first attempt to load a large number (2500) of images, then this may help.

Edit > Preferences

Find Performance tab
1. #### Under heading Camera Raw
   
   Turn Off 'Use GPU for Preview Generation'
   
2. #### Under heading Camera Raw Cache Settings
  
   Change location to something like D:\LR_Cache
   
   And make 'Maximum Size:100 GB

## Catalog
Delete this folder to remove catalog (deletes LR database and edits), this will enable you to re-import images as if first time import
1. C:\Users\username\Pictures\Lightroom


![Badge Description](https://img.shields.io/github/last-commit/berlinbabel/aerial_workflow)

[README](../README.md)
