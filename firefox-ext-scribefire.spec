%define ff_epoch 0
%define ff_ver 3.0.6

%define _mozillapath %{_libdir}/firefox-%{ff_ver}
%define _mozillaextpath %{_mozillapath}/extensions

Summary: ScribeFire extension for firefox
Name: firefox-ext-scribefire
Version: 3.1.6
Release: %mkrel 1
License: GPLv2
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/1730
Source: http://releases.mozilla.org/pub/mozilla.org/addons/1730/scribefire-%version-fx+sm.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: mozilla-firefox = %{ff_epoch}:%{ff_ver}
Obsoletes: mozilla-firefox-ext-scribefire < %{version}-%{release}
Provides: mozilla-firefox-ext-scribefire = %{version}-%{release}

%description
ScribeFire (previously Performancing for Firefox) is a full-featured blog
editor that integrates with your browser and lets you easily post to your blog.
You can drag and drop formatted text from pages you are browsing, take notes,
and post to your blog.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %_mozillapath
%{_mozillaextpath}
