Due to MD5 sum inconsistencies between Groovy and Indigo moveit messages, this package helps overcome this barrier.

The follow joint trajectory messages created by this package will have the same MD5sum as Groovy messages.  

A pr2_moveit fork has been created to take advantage of the now-compatible follow joint trajectory messges under https://githb.com/abrinkmacmu/moveit_pr2.git. This is also referenced in the rosinstall file and can be fetched using wstool:

	$ wstool update -t <path/to/groovy_indigo_moveit_wrapper>


For a visual description of the data flow, checkout groovy_indigo_move_wrapper/doc/