`. To do so, you'll navigate to the listeners navigation page and select the "Profiles" tab:

![Profiles Table](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-profiles.png)

To create a new profile, click on the "Create" button. To edit a particular profile, click on the name of the profile. Keep in mind, that you cannot edit profiles that are associated with active listeners.

After clicking "Create", select the "BridgeProfile" tab:

![Create BridgeProfile](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-bridgeprofilecreate.png)

The following options will need to be configured when editing or creating a profile:

* **Name** - The `

` of the profile that will be used throughout the interface. Pick something recognizable!
* **Description** - The `

` of the profile. This should be a thorough description of the profile that operators can read and easily understand how the profile works, and the use cases for which it would be appropriate to use the profile. 
* **MessageTransform** - The `

`.
* **ReadFormat** - The `

` is the format of a message when a Grunt reads data from a C2Bridge. The format must include a location for the data and Grunt GUID to be placed. Include the string "{DATA}" to indicate the location that the data should be placed and the string "{GUID}" to indicate the location that the GUID should be placed.
* **WriteFormat** - The `

` is the format of a message when a Grunt writes data to a C2Bridge. The format must include a location for the data and Grunt GUID to be placed. Include the string "{DATA}" to indicate the location that the data should be placed and the string "{GUID}" to indicate the location that the GUID should be placed.
* **BridgeMessengerCode** - The `

