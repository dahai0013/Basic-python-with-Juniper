# This script will create 2k AE/LAG sub-interface on juniper router/switches

<description of the project at creation time >



## Getting Started

    Phase 1-
    Phase 2-

## Prerequisites

  none


## Phase 1

    1- create the credential file and point the scpt to the correct file
    2- create and ae0 ( if different change the script )
    3- at this stage I run the script from pycharm




    set interfaces ae0 flexible-vlan-tagging
    set interfaces ae0 aggregated-ether-options minimum-links 1
    set interfaces ae0 aggregated-ether-options link-speed 10g

    set interfaces xe-1/0/1 gigether-options 802.3ad ae0
    set interfaces xe-1/0/2 gigether-options 802.3ad ae0


## Phase 2

    1-  remove the ae0
    2-
    3-


    #delete interfaces ae0


##  python script manual information:





## Contributing

Everyone is welcome ;-)


## Versioning

Beta version

## Authors

* Me, Myself and I ( https://www.youtube.com/watch?v=P8-9mY-JACM )


## License

Free Code Forever and Wakanda.

## Acknowledgments

* Python Team and Linus Torvalds
* Youtuber, Blogger and contributor of all type
* and You