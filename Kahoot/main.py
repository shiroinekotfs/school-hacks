from scripts.sprint import sprint
from scripts.colors import ran, y, r, g, c
from subprocess import call
import time
import os
from os import system


print("\n" * 128)
print(f"{g}                                                         {y}▄▄ ▄████▄▐▄▄▄▌           ")
print(f"            {y}▄▀▄     ▄▀▄                                 {y}▐  ████▀███▄█▄▌           ")
print(f"           {y}▄█░░▀▀▀▀▀░░█▄                              {y}▐ ▌  █▀▌  ▐▀▌▀█▀            ")
print(f"       {y}▄▄  █░░░░░░░░░░░█  ▄▄        {g}//+++\\             {y}▀   ▌ ▌  ▐ ▌            ")
print(f"      {y}█▄▄█ █░░▀░░┬░░▀░░█ █▄▄█     {g}//  ||| \\                {y}█ █  ▐▌█         {g}")
print("██╗░░██╗██╗████████╗████████╗██╗░░░██╗|||████████╗░█████╗░░█████╗░██╗░░░░░░██████╗")
print("██║░██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗░██╔╝|||╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝")
print("█████═╝░██║░░░██║░░░░░░██║░░░░╚████╔╝░|||░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░")
print("██╔═██╗░██║░░░██║░░░░░░██║░░░░░╚██╔╝░░|||░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗")
print("██║░╚██╗██║░░░██║░░░░░░██║░░░░░░██║░░░|||░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝")
print("╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░|||░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░")
print("Kahoot Hacks            \\             |||             //                         ")
print("                         \\            |||            //                          ")
print("                          \\           |||           //                           ")
print("                           \\          |||          //                            ")
print("                     /===================================\\                       ")
print(f"                   //              {r}  -Fun-              {g}  \\               ")
print(f"                  ||                {r}-Hacks-            {g}   ||               ")
print(f"                  ||                {r} -For-             {g}   ||               ")
print(f"                  ||                 {r}-The-             {g}   ||               ")
print(f"                  ||                {r}-Whole-            {g}   ||               ")
print(f"                   \\                {r}-Family-           {g}  //               ")
print("                    \\====================================/                       ")
print(" ")
print(f"{y}|======= {r}News{y} =======| ")
print(f"|{y}Want to help... do this; {r} create an issue, tell me your idea, ither you or i can make it... {y}You will get credit for your work")
print(f"{r}|=========================| ")
print(" ")
print(" ")
print(" ")
time.sleep(2)
print(" ")
sprint(f"{g}Please type 1, 2, 3, or {y}4{g}")
print(" ")
print("[1] How to use")
print("||| \\--------/")
print(" ")
print("[2] Information")
print("||| \\---------/")
print(" ")
print("[3] Flooder (Getting Updated!)")
print("||| \\-----/")
print(" ")
print(f"[4] {y}Start Hack")
print(f"{c}||| {g}\\--------/")
choice = input("")


if choice == "1":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/HTU.py"])

if choice == "2":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/Info.py"])

if choice == "3":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/flood/Info.py"])

if choice == "4":
    print(" ")
    print("Starting...")
    time.sleep(1)
    print("\n" * 64)  # imma this makes more sense
    call(["python", "Kahoot/kahoot.py"])

time.sleep(25)
print(" ")
print(" ")
print("Program Made by CPScript")
print(" ")
print("   ▄▀ ▄▀   ")
print("    ▀  ▀   ")
print("  █▀▀▀▀▀█▄ ")
print("  █░░░░░█ █")
print("  ▀▄▄▄▄▄▀▀ ")
