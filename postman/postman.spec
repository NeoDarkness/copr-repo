%global debug_package %{nil}

%global __provides_exclude_from ^/opt/Postman/.*$
%global __requires_exclude_from ^/opt/Postman/.*$

Name:           postman
Version:        12.19.3
Release:        %autorelease
Summary:        Postman API Platform

License:        LicenseRef-postman-eula
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Postman is an API platform for building and using APIs.

%prep
%autosetup -n Postman

%build

%install
install -d %{buildroot}/opt/Postman
cp -a . %{buildroot}/opt/Postman/

install -d %{buildroot}%{_bindir}
ln -s ../../opt/Postman/Postman %{buildroot}%{_bindir}/postman

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}

install -Dpm 0644 app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/postman.png

%check

%files
/opt/Postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/icons/hicolor/128x128/apps/postman.png

%changelog
%autochangelog