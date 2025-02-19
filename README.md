# **Random Adventure**

## Project Notes 02/18/2025

> Update 2: Commented everything out to attempt to go another way
> realizing I didn't need to do that. For now, putting this project
> on hold while starting fresh. Organizing everything got gears 
> turning, for better or worse and I need to see where it goes
> before building off this. If the muse hit, this will be shelved.
> If it didn't, I'll pick this up again. 
>
> Update 1: Had a little time before work to do some more clean up in the main.
> Moved some blocks of narration to their own functions and created an
> insert_line function to break up input prompts from the narration.
> Didn't break anything in the process. 

## Project Notes 02/17/2025

> Update 2: Created a file to store the functions. Made a couple new
> ones. The main is cleaning up and nothing seems to have broke in
> the process. Productive day.
> 
> ***Plans for Tomorrow*** Rework the invalid input for name selection
> so the Narrator chooses a name at random instead of forcing the player
> to use their first input. This will bypass that potential issue with
> pressing [ENTER] since there is no second prompt to correct it and
> it'll give the Narrator more personality development. We love the
> Narrator. Shooting for comedy gold.
>
> Update 1: Took some advice from Danny @ Code: You and decided to
> dabble in oop for some object handling. Removed the list
> created to hold hero info and created a class file. Created
> a Hero class to use instead of a list - used said class to 
> iron out naming and changing character name. Everything looks
> good so far.  
> 
> ***Potential Issue:*** During the type_narration function on naming the
> hero, if the player hits [ENTER] thinking they can speed up/bypass
> the char by char display...the players name defaults blank in the
> initial dialogue. They are prompted for a name change after so I 
> don't know how bothered I am by it.  I did look to see if there was
> a way to prevent that from happening with no luck - I either need to
> Google harder or accept it's just going to be that way. Can I accept that?
> Only time will tell. It's eventually going to need fixed.

## Project Notes 02/16/2025
> Update 2: Deleted over 100 lines of code and reworked
> the menus.  It's a thing of beauty now, and it is not to be
> changed. It's fine. **Remember it's fine**. Adding additional
> menus later is acceptable, just don't screw with the logic.
> 
> Update 1: Got the main menu set up and began working on
> the main process of the program - player naming
> seems to be ironed out. Checked off creation of
> the base class.

## Project Notes 02/15/2025
> Created as python practice during Code:You -
> the concept is to create a text base rpg. Work 
> today is set aside for general concepts. 
>- [x] Create Base Class (Melee)
>   - [ ] equipment
>   - [ ] inventory
>   - [ ] status
>- [ ] Starting Village
>   - [ ] Home
>   - [ ] Shops
>   - [ ] Jobs
>   - [ ] Tavern
>   - [ ] House of Worship
>- [ ] Surrounding Area
>   - [ ] Hostile Creatures/Leveling
>   - [ ] Area to execute jobs
