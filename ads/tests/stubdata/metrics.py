# coding=utf-8
"""
Metrics service example response
"""

example_metrics_response='''{
  "basic stats": {
    "average number of downloads": 79.0,
    "average number of reads": 111.0,
    "median number of downloads": 79.0,
    "median number of reads": 111.0,
    "normalized paper count": 1.0,
    "number of papers": 1,
    "recent number of downloads": 0,
    "recent number of reads": 2,
    "total number of downloads": 79,
    "total number of reads": 111
  },
  "basic stats refereed": {
    "average number of downloads": 79.0,
    "average number of reads": 111.0,
    "median number of downloads": 79.0,
    "median number of reads": 111.0,
    "normalized paper count": 1.0,
    "number of papers": 1,
    "recent number of downloads": 0,
    "recent number of reads": 2,
    "total number of downloads": 79,
    "total number of reads": 111
  },
  "citation stats": {
    "average number of citations": 66.0,
    "average number of refereed citations": 64.0,
    "median number of citations": 66.0,
    "median number of refereed citations": 64.0,
    "normalized number of citations": 66.0,
    "normalized number of refereed citations": 64.0,
    "number of citing papers": 66,
    "number of self-citations": 0,
    "total number of citations": 66,
    "total number of refereed citations": 64
  },
  "citation stats refereed": {
    "average number of citations": 66.0,
    "average number of refereed citations": 64.0,
    "median number of citations": 66.0,
    "median number of refereed citations": 64.0,
    "normalized number of citations": 66.0,
    "normalized number of refereed citations": 64.0,
    "number of citing papers": 66,
    "number of self-citations": 0,
    "total number of citations": 66,
    "total number of refereed citations": 64
  },
  "histograms": {
    "citations": {
      "nonrefereed to nonrefereed": {
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "nonrefereed to nonrefereed normalized": {
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "nonrefereed to refereed": {
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 1,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 1,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "nonrefereed to refereed normalized": {
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 1.0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 1.0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "refereed to nonrefereed": {
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "refereed to nonrefereed normalized": {
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "refereed to refereed": {
        "1981": 4,
        "1982": 3,
        "1983": 3,
        "1984": 3,
        "1985": 7,
        "1986": 4,
        "1987": 6,
        "1988": 7,
        "1989": 1,
        "1990": 4,
        "1991": 2,
        "1992": 1,
        "1993": 1,
        "1994": 4,
        "1995": 0,
        "1996": 2,
        "1997": 1,
        "1998": 2,
        "1999": 3,
        "2000": 1,
        "2001": 1,
        "2002": 1,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 1,
        "2007": 0,
        "2008": 0,
        "2009": 1,
        "2010": 0,
        "2011": 0,
        "2012": 1,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "refereed to refereed normalized": {
        "1981": 4.0,
        "1982": 3.0,
        "1983": 3.0,
        "1984": 3.0,
        "1985": 7.0,
        "1986": 4.0,
        "1987": 6.0,
        "1988": 7.0,
        "1989": 1.0,
        "1990": 4.0,
        "1991": 2.0,
        "1992": 1.0,
        "1993": 1.0,
        "1994": 4.0,
        "1995": 0,
        "1996": 2.0,
        "1997": 1.0,
        "1998": 2.0,
        "1999": 3.0,
        "2000": 1.0,
        "2001": 1.0,
        "2002": 1.0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 1.0,
        "2007": 0,
        "2008": 0,
        "2009": 1.0,
        "2010": 0,
        "2011": 0,
        "2012": 1.0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      }
    },
    "downloads": {
      "all downloads": {
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 2,
        "2000": 4,
        "2001": 2,
        "2002": 9,
        "2003": 4,
        "2004": 12,
        "2005": 4,
        "2006": 6,
        "2007": 3,
        "2008": 11,
        "2009": 4,
        "2010": 2,
        "2011": 7,
        "2012": 4,
        "2013": 2,
        "2014": 3,
        "2015": 0
      },
      "all downloads normalized": {
        "1996": 0.0,
        "1997": 0.0,
        "1998": 0.0,
        "1999": 2.0,
        "2000": 4.0,
        "2001": 2.0,
        "2002": 9.0,
        "2003": 4.0,
        "2004": 12.0,
        "2005": 4.0,
        "2006": 6.0,
        "2007": 3.0,
        "2008": 11.0,
        "2009": 4.0,
        "2010": 2.0,
        "2011": 7.0,
        "2012": 4.0,
        "2013": 2.0,
        "2014": 3.0,
        "2015": 0.0
      },
      "refereed downloads": {
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 2,
        "2000": 4,
        "2001": 2,
        "2002": 9,
        "2003": 4,
        "2004": 12,
        "2005": 4,
        "2006": 6,
        "2007": 3,
        "2008": 11,
        "2009": 4,
        "2010": 2,
        "2011": 7,
        "2012": 4,
        "2013": 2,
        "2014": 3,
        "2015": 0
      },
      "refereed downloads normalized": {
        "1996": 0.0,
        "1997": 0.0,
        "1998": 0.0,
        "1999": 2.0,
        "2000": 4.0,
        "2001": 2.0,
        "2002": 9.0,
        "2003": 4.0,
        "2004": 12.0,
        "2005": 4.0,
        "2006": 6.0,
        "2007": 3.0,
        "2008": 11.0,
        "2009": 4.0,
        "2010": 2.0,
        "2011": 7.0,
        "2012": 4.0,
        "2013": 2.0,
        "2014": 3.0,
        "2015": 0.0
      }
    },
    "publications": {
      "all publications": {
        "1980": 1,
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "all publications normalized": {
        "1980": 1.0,
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "refereed publications": {
        "1980": 1,
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      },
      "refereed publications normalized": {
        "1980": 1.0,
        "1981": 0,
        "1982": 0,
        "1983": 0,
        "1984": 0,
        "1985": 0,
        "1986": 0,
        "1987": 0,
        "1988": 0,
        "1989": 0,
        "1990": 0,
        "1991": 0,
        "1992": 0,
        "1993": 0,
        "1994": 0,
        "1995": 0,
        "1996": 0,
        "1997": 0,
        "1998": 0,
        "1999": 0,
        "2000": 0,
        "2001": 0,
        "2002": 0,
        "2003": 0,
        "2004": 0,
        "2005": 0,
        "2006": 0,
        "2007": 0,
        "2008": 0,
        "2009": 0,
        "2010": 0,
        "2011": 0,
        "2012": 0,
        "2013": 0,
        "2014": 0,
        "2015": 0
      }
    },
    "reads": {
      "all reads": {
        "1996": 0,
        "1997": 0,
        "1998": 2,
        "1999": 5,
        "2000": 4,
        "2001": 4,
        "2002": 14,
        "2003": 5,
        "2004": 14,
        "2005": 4,
        "2006": 8,
        "2007": 5,
        "2008": 13,
        "2009": 7,
        "2010": 3,
        "2011": 9,
        "2012": 5,
        "2013": 3,
        "2014": 4,
        "2015": 2
      },
      "all reads normalized": {
        "1996": 0.0,
        "1997": 0.0,
        "1998": 2.0,
        "1999": 5.0,
        "2000": 4.0,
        "2001": 4.0,
        "2002": 14.0,
        "2003": 5.0,
        "2004": 14.0,
        "2005": 4.0,
        "2006": 8.0,
        "2007": 5.0,
        "2008": 13.0,
        "2009": 7.0,
        "2010": 3.0,
        "2011": 9.0,
        "2012": 5.0,
        "2013": 3.0,
        "2014": 4.0,
        "2015": 2.0
      },
      "refereed reads": {
        "1996": 0,
        "1997": 0,
        "1998": 2,
        "1999": 5,
        "2000": 4,
        "2001": 4,
        "2002": 14,
        "2003": 5,
        "2004": 14,
        "2005": 4,
        "2006": 8,
        "2007": 5,
        "2008": 13,
        "2009": 7,
        "2010": 3,
        "2011": 9,
        "2012": 5,
        "2013": 3,
        "2014": 4,
        "2015": 2
      },
      "refereed reads normalized": {
        "1996": 0.0,
        "1997": 0.0,
        "1998": 2.0,
        "1999": 5.0,
        "2000": 4.0,
        "2001": 4.0,
        "2002": 14.0,
        "2003": 5.0,
        "2004": 14.0,
        "2005": 4.0,
        "2006": 8.0,
        "2007": 5.0,
        "2008": 13.0,
        "2009": 7.0,
        "2010": 3.0,
        "2011": 9.0,
        "2012": 5.0,
        "2013": 3.0,
        "2014": 4.0,
        "2015": 2.0
      }
    }
  },
  "indicators": {
    "g": 1,
    "h": 1,
    "i10": 1,
    "i100": 0,
    "m": 0.027777777777777776,
    "read10": 0,
    "riq": 47,
    "tori": 2.9132693515578443
  },
  "indicators refereed": {
    "g": 1,
    "h": 1,
    "i10": 1,
    "i100": 0,
    "m": 0.027777777777777776,
    "read10": 0,
    "riq": 47,
    "tori": 2.9132693515578443
  },
  "skipped bibcodes": [],
  "time series": {
    "g": {
      "1980": 0,
      "1981": 0,
      "1982": 0,
      "1983": 0,
      "1984": 0,
      "1985": 0,
      "1986": 0,
      "1987": 0,
      "1988": 0,
      "1989": 0,
      "1990": 0,
      "1991": 0,
      "1992": 0,
      "1993": 0,
      "1994": 0,
      "1995": 0,
      "1996": 0,
      "1997": 0,
      "1998": 0,
      "1999": 0,
      "2000": 0,
      "2001": 0,
      "2002": 0,
      "2003": 0,
      "2004": 0,
      "2005": 0,
      "2006": 0,
      "2007": 0,
      "2008": 0,
      "2009": 0,
      "2010": 0,
      "2011": 0,
      "2012": 0,
      "2013": 0,
      "2014": 0,
      "2015": 0
    },
    "h": {
      "1980": 0,
      "1981": 0,
      "1982": 0,
      "1983": 0,
      "1984": 0,
      "1985": 0,
      "1986": 0,
      "1987": 0,
      "1988": 0,
      "1989": 0,
      "1990": 0,
      "1991": 0,
      "1992": 0,
      "1993": 0,
      "1994": 0,
      "1995": 0,
      "1996": 0,
      "1997": 0,
      "1998": 0,
      "1999": 0,
      "2000": 0,
      "2001": 0,
      "2002": 0,
      "2003": 0,
      "2004": 0,
      "2005": 0,
      "2006": 0,
      "2007": 0,
      "2008": 0,
      "2009": 0,
      "2010": 0,
      "2011": 0,
      "2012": 0,
      "2013": 0,
      "2014": 0,
      "2015": 0
    },
    "i10": {
      "1980": 0,
      "1981": 0,
      "1982": 0,
      "1983": 1,
      "1984": 1,
      "1985": 1,
      "1986": 1,
      "1987": 1,
      "1988": 1,
      "1989": 1,
      "1990": 1,
      "1991": 1,
      "1992": 1,
      "1993": 1,
      "1994": 1,
      "1995": 1,
      "1996": 1,
      "1997": 1,
      "1998": 1,
      "1999": 1,
      "2000": 1,
      "2001": 1,
      "2002": 1,
      "2003": 1,
      "2004": 1,
      "2005": 1,
      "2006": 1,
      "2007": 1,
      "2008": 1,
      "2009": 1,
      "2010": 1,
      "2011": 1,
      "2012": 1,
      "2013": 1,
      "2014": 1,
      "2015": 1
    },
    "i100": {
      "1980": 0,
      "1981": 0,
      "1982": 0,
      "1983": 0,
      "1984": 0,
      "1985": 0,
      "1986": 0,
      "1987": 0,
      "1988": 0,
      "1989": 0,
      "1990": 0,
      "1991": 0,
      "1992": 0,
      "1993": 0,
      "1994": 0,
      "1995": 0,
      "1996": 0,
      "1997": 0,
      "1998": 0,
      "1999": 0,
      "2000": 0,
      "2001": 0,
      "2002": 0,
      "2003": 0,
      "2004": 0,
      "2005": 0,
      "2006": 0,
      "2007": 0,
      "2008": 0,
      "2009": 0,
      "2010": 0,
      "2011": 0,
      "2012": 0,
      "2013": 0,
      "2014": 0,
      "2015": 0
    },
    "read10": {
      "1980": 0.0,
      "1981": 0.0,
      "1982": 0.0,
      "1983": 0.0,
      "1984": 0.0,
      "1985": 0.0,
      "1986": 0.0,
      "1987": 0.0,
      "1988": 0.0,
      "1989": 0.0,
      "1990": 0.0,
      "1991": 0.0,
      "1992": 0.0,
      "1993": 0.0,
      "1994": 0.0,
      "1995": 0.0,
      "1996": 0,
      "1997": 0,
      "1998": 0,
      "1999": 0,
      "2000": 0,
      "2001": 0,
      "2002": 0,
      "2003": 0,
      "2004": 0,
      "2005": 0,
      "2006": 0,
      "2007": 0,
      "2008": 0,
      "2009": 0,
      "2010": 0,
      "2011": 0,
      "2012": 0,
      "2013": 0,
      "2014": 0,
      "2015": 0.0
    },
    "tori": {
      "1980": 0.0,
      "1981": 0.4720238095238095,
      "1982": 0.5856664212076583,
      "1983": 0.8958737577307843,
      "1984": 1.0222508289354417,
      "1985": 1.2338053118559293,
      "1986": 1.3881897427207974,
      "1987": 1.7795326046518947,
      "1988": 2.021415312515987,
      "1989": 2.061415312515987,
      "1990": 2.3636195410360052,
      "1991": 2.3976064691405803,
      "1992": 2.4270182338464625,
      "1993": 2.479649812793831,
      "1994": 2.574924230722711,
      "1995": 2.574924230722711,
      "1996": 2.6006982366947367,
      "1997": 2.614983950980451,
      "1998": 2.6688457395983374,
      "1999": 2.6995311545967735,
      "2000": 2.8718000621597985,
      "2001": 2.879262748726963,
      "2002": 2.8956561913499135,
      "2003": 2.8956561913499135,
      "2004": 2.8956561913499135,
      "2005": 2.8956561913499135,
      "2006": 2.902799048492771,
      "2007": 2.902799048492771,
      "2008": 2.902799048492771,
      "2009": 2.9116486060148947,
      "2010": 2.9116486060148947,
      "2011": 2.9116486060148947,
      "2012": 2.9132693515578443,
      "2013": 2.9132693515578443,
      "2014": 2.9132693515578443,
      "2015": 2.9132693515578443
    }
  }
}'''