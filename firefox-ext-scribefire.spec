Summary:	ScribeFire extension for firefox
Name:		firefox-ext-scribefire
Version:	4.0
Release:	12
License:	GPLv2
Group:		Networking/WWW
Url:		https://addons.mozilla.org/en-US/firefox/addon/scribefire-next/
Source0:	http://releases.mozilla.org/pub/mozilla.org/addons/1730/scribefire_next-%{version}-fx.xpi
Buildarch:	noarch

BuildRequires:	firefox-devel
Requires:	firefox >= %{firefox_version}

%description
ScribeFire (previously Performancing for Firefox) is a full-featured blog
editor that integrates with your browser and lets you easily post to your blog.
You can drag and drop formatted text from pages you are browsing, take notes,
and post to your blog.

%prep
%setup -q -c

%install
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

%files
%{firefox_extdir}

