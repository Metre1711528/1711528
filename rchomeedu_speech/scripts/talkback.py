#!/usr/bin/env python

"""
    talkback.py - Version 1.1 2013-12-20
    
    Use the sound_play client to say back what is heard by the pocketsphinx recognizer.
    
"""

import rospy, os, sys
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient
global i

class TalkBack:
    def __init__(self, script_path):
        rospy.init_node('talkback')
	
        rospy.on_shutdown(self.cleanup)
        
        # Create the sound client object
        self.soundhandle = SoundClient()
        
        # Wait a moment to let the client connect to the
        # sound_play server
        rospy.sleep(1)
        
        # Make sure any lingering sound_play processes are stopped.
        self.soundhandle.stopAll()
        
        # Announce that we are ready for input
        #self.soundhandle.playWave('say-beep.wav')
        #rospy.sleep(2)
        #self.soundhandle.say('Ready')
        
        rospy.loginfo("Say one of the navigation commands...")

        # Subscribe to the recognizer output and set the callback function
	#self.pubs = rospy.Publisher("state", bool, queue_size=10)
	#self.pubs.publish(true)
	if i == 1:
	    rospy.Subscriber('/lm_data', String, self.talkback, queue_size=1)
	
		
    def talkback(self, msg):
        # Print the recognized words on the screen
        rospy.loginfo(msg.data)
        #self.pubs.publish(false)
        # Speak the recognized words in the selected voice
	i = 0
	if msg.data != '0':
	    if msg.data.find('WHO ARE YOU')>-1:
		self.soundhandle.say("I heard you ask about my name.I am Alice,a robot.what's your name?")
		#rospy.sleep(8)
	    elif msg.data.find('I AM')>-1:
		self.soundhandle.say("nice to meet you.")
                #rospy.sleep(5)
	    elif msg.data.find('EXCUSE')>-1:
		self.soundhandle.say("What can I help you?")
                #rospy.sleep(5)
	    elif msg.data.find('HELLO')>-1:
		self.soundhandle.say("hi.")
                #rospy.sleep(5)
	    elif msg.data.find('THANK')>-1:
		self.soundhandle.say("You are welcome.")
                #rospy.sleep(5)
	    elif msg.data.find('ARE YOU FROM')>-1:
		self.soundhandle.say("I am from China!")
		#rospy.sleep(5)
	    elif msg.data.find('HOW OLD')>-1:
                self.soundhandle.say("I'm three years old.")
		#rospy.sleep(5)
	    elif msg.data.find('CAN YOU DO')>-1:
		self.soundhandle.say("I can only talk with you now.But I will learn more skills!")
		#rospy.sleep(8)
	    rospy.sleep(8)
	i = 1
	#self.pubs.publish(true)

    def cleanup(self):
        self.soundhandle.stopAll()
        rospy.loginfo("Shutting down talkback node...")

if __name__=="__main__":
    i = 1
    try:
        TalkBack(sys.path[0])
	
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Talkback node terminated.")
