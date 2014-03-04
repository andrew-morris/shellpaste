shellpaste
==========

## Summary

Tiny snippet of code that pulls ASCII shellcode from pastebin and executes it. The purpose of this is to have a minimal amount of benign code so AV doesn't freak out, then it pulls down the evil stuff. People have been doing this kind of stuff for years so I take no credit for the concept. That being said, this code (or similar code) works surprisingly often during pentests when conventional malware fails. 

## Usage

Upload your ASCII shellcode to pastebin, edit the path in the code, then compile with py2exe or pyinstaller.

## Disclaimer

Don't use this for anything illegal, please. I take no responsibility, blah blah blah.
