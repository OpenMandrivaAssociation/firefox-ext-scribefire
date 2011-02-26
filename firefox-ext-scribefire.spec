Summary: ScribeFire extension for firefox
Name: firefox-ext-scribefire
Version: 3.5.3.3
Release: %mkrel 2
License: GPLv2
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/1730
Source: http://releases.mozilla.org/pub/mozilla.org/addons/1730/scribefire-%version-fx.xpi
Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_epoch}:%{firefox_version}
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
