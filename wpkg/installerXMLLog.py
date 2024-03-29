from elementtree.SimpleXMLWriter import XMLWriter

def installerLog(package_details):
    '''
    This module writes the required fields of a package to a temporary 
    XML file which is then appended to the list of installedLog.xml.
    Right now - only name and version written to the installedLog.xml.
    '''
    
    #package_details contain all the info about the package
    w = XMLWriter('tempholder.xml')
    xml = w.start("xml")
    w.start("Package")
    w.element("name", package_details[0])
    w.element("version", package_details[1])
    #w.element("architecture", package_details[2])
    #w.element("short-description",package_details[3])
    #w.element("installed",package_details[4])
    #w.element("long-description",package_details[4])
    #-----^basic logging data above^------
    #w.element("section",package_details[5])
    #w.element("installed-size",package_details[6])
    #w.element("maintainer",package_details[7])
    #w.element("original-maintainer",package_details[8])
    #w.element("replaces",package_details[9])
    #w.element("provides",package_details[10])
    #w.element("pre-depends",package_details[11])
    #w.element("depends",package_details[5])
    #w.element("recomends",package_details[13])
    #w.element("suggests",package_details[14])
    #w.element("conflicts",package_details[15])
    #w.element("filename",package_details[16])
    #w.element("size",package_details[17])
    #w.element("md5sum",package_details[18])
    #w.element("homepage",package_details[19])
    w.end()
    w.close(xml)
