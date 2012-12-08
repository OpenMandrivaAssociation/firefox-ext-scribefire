Summary: ScribeFire extension for firefox
Name: firefox-ext-scribefire
Version: 4.0
Release: 6
License: GPLv2
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/1730
Source: http://releases.mozilla.org/pub/mozilla.org/addons/1730/scribefire_next-%version-fx.xpi
Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_version}
Obsoletes: mozilla-firefox-ext-scribefire < %{version}-%{release}
Provides: mozilla-firefox-ext-scribefire = %{version}-%{release}
Obsoletes: firefox-ext-scribefire < %{version}-%{release}
BuildRequires: firefox-devel

%description
ScribeFire (previously Performancing for Firefox) is a full-featured blog
editor that integrates with your browser and lets you easily post to your blog.
You can drag and drop formatted text from pages you are browsing, take notes,
and post to your blog.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.5.3.3-3mdv2011.0
+ Revision: 664310
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 3.5.3.3-2
+ Revision: 640061
- rebuild

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 3.5.3.3-1
+ Revision: 631496
- new version 3.5.3.3

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 3.5.3.1-4mdv2011.0
+ Revision: 628877
- rebuild for new firefox

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 3.5.3.1-3mdv2011.0
+ Revision: 597398
- rebuild for new firefox

* Sun Sep 19 2010 Funda Wang <fwang@mandriva.org> 3.5.3.1-2mdv2011.0
+ Revision: 579785
- rebuild

* Thu Sep 02 2010 Funda Wang <fwang@mandriva.org> 3.5.3.1-1mdv2011.0
+ Revision: 575508
- new version 3.5.3.1

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 3.5.2-3mdv2011.0
+ Revision: 561169
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 3.5.2-2mdv2010.1
+ Revision: 549356
- rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - new version 3.5.2

* Wed Apr 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5.1-2mdv2010.1
+ Revision: 532637
- don't provide empty debug package

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 3.5.1-1mdv2010.1
+ Revision: 531238
- update to new version 3.5.1

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 3.4.6-4mdv2010.1
+ Revision: 531078
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 3.4.6-3mdv2010.1
+ Revision: 526991
- rebuild

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 3.4.6-2mdv2010.1
+ Revision: 494800
- rebuild

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 3.4.6-1mdv2010.1
+ Revision: 480374
- new version 3.4.6 (ff 3.6b5)

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 3.4.5-3mdv2010.1
+ Revision: 479192
- rebuild for new ff

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 3.4.5-2mdv2010.1
+ Revision: 462799
- rebuild for new ff

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 3.4.5-1mdv2010.0
+ Revision: 443371
- new version 3.4.5
- rebuild for new ff

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 3.4.1-4mdv2010.0
+ Revision: 417673
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Tue Aug 04 2009 Eugeni Dodonov <eugeni@mandriva.com> 3.4.1-3mdv2010.0
+ Revision: 408636
- rebuild for firefox 3.0.13

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 3.4.1-2mdv2010.0
+ Revision: 405034
- rebuild for new ff

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 3.4.1-1mdv2010.0
+ Revision: 385777
- New version 3.4.1

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 3.3.1-1mdv2010.0
+ Revision: 381247
- New version 3.3.1

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 3.3-1mdv2010.0
+ Revision: 369620
- renew tarball
- New version 3.3

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 3.2.3-2mdv2009.1
+ Revision: 361853
- rebuild for firefox 3.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 3.2.3-1mdv2009.1
+ Revision: 354096
- New version 3.2.3

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 3.1.6-1mdv2009.1
+ Revision: 337295
- rename to firefox
- rename to firefox
- new version 3.1.6

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 3.1.3-2mdv2009.1
+ Revision: 318923
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 3.1.3-1mdv2009.1
+ Revision: 303707
- new version 3.1.3

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 2.3.1-2mdv2009.0
+ Revision: 289185
- rebuild for new FF

* Tue Aug 12 2008 Funda Wang <fwang@mandriva.org> 2.3.1-1mdv2009.0
+ Revision: 271163
- New version 2.3.1

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 2.3-1mdv2009.0
+ Revision: 258224
- New version 2.3

* Wed Jul 30 2008 Tiago Salem <salem@mandriva.com.br> 2.2.7-4mdv2009.0
+ Revision: 256468
- add conditional to ff3

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.7-3mdv2009.0
+ Revision: 236323
- rebuilt for mozilla-firefox-2.0.0.16

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 2.2.7-2mdv2009.0
+ Revision: 231261
- Rebuild for firefox 2.0.0.15

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 2.2.7-1mdv2009.0
+ Revision: 229995
- New version 2.2.7

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 2.1-1mdv2009.0
+ Revision: 201023
- New version 2.1

* Fri Apr 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-7mdv2009.0
+ Revision: 195595
- rebuild for mozilla-firefox-2.0.0.14

* Wed Mar 26 2008 Tiago Salem <salem@mandriva.com.br> 1.4.2-6mdv2008.1
+ Revision: 190331
- bump ff_ver and release

* Fri Mar 07 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.4.2-5mdv2008.1
+ Revision: 181497
- Rebuilt against FF 2.0.0.12

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 1.4.2-4mdv2008.1
+ Revision: 117796
- own firefox directories so that they're not left behind on uninstall

* Tue Dec 11 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.4.2-3mdv2008.1
+ Revision: 117476
- Rebuilt for FF 2.0.0.11

* Mon Nov 05 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.4.2-2mdv2008.1
+ Revision: 106120
- New firefox: 2.0.0.9

* Fri Oct 19 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.4.2-1mdv2008.1
+ Revision: 100398
- New upstream: 1.4.2
- Rebuilt against FF 2.0.0.8

* Wed Aug 01 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.4.1-1mdv2008.0
+ Revision: 57665
- Building for FF 2.0.0.6
- Import mozilla-firefox-ext-scribefire

