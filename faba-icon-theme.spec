Name:           faba-icon-theme
Version:        4.1.2
Release:        1%{?dist}
Summary:        Faba Icon theme

License:        LGPL-3.0+ or CC-BY-SA-4.0
URL:            https://snwh.org/moka
Source0:        https://github.com/snwh/faba-icon-theme/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  automake
BuildRequires:  icon-naming-utils
BuildRequires:  gtk2
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme

%description
Faba is a sexy and modern icon theme with Tango influences. All variations and
supplementary themes for Faba, require this base theme.


%prep
%setup -q
chmod +x autogen.sh
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc AUTHORS README.md
%license COPYING LICENSE
%{_datadir}/icons/Faba
%ghost %{_datadir}/icons/Faba/icon-theme.cache


%post
touch --no-create %{_datadir}/icons/Faba &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/Faba &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/Faba &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Faba &>/dev/null || :


%changelog
* Tue Sep 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 4.1.2-1
- Public release
